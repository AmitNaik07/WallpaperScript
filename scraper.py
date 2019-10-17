from bs4 import BeautifulSoup as bs
import urllib.request
import re
import random

# these are the search tags for the respective seasons
weather_tags = {
    "CLEAR"   :   "clearweather",
    "MIST"    :   "fog",
    "DRIZZLE" :   "rain",
    "SNOW"    :   "snow",
    "THUNDER" :   "thunderstorm"
    }

# smaller the faster, but with repeated images
IMAGES_TO_ITERATE_OVER = 10

'''
Searches over flickr using Beautiful Soup, parses the query to get the relevant picture.

input
season: from weather_tags, acts as a such search term

return
url of the image
'''
def get_image_url_from_flickr(season="CLEAR"):
    # search flickr to get the relevant image
    base_url =  "https://www.flickr.com/search/?text="
    get_url = "https://www.flickr.com/search/?text="+weather_tags[season]

    # bs4 magic
    html = urllib.request.urlopen(get_url).read()
    soup = bs(html,'html.parser')
    div_tags = soup('div')

    # randomizing the image
    count = random.randint(1,IMAGES_TO_ITERATE_OVER)
    for item in div_tags:
        class_attribute = item.get('class')
        '''
        Parsing this: 
        <div class="view photo-list-photo-view requiredToShowOnServer awake" data-view-signature="photo-list-photo-view__UA_1__adConfig_1__engagementModelName_photo-lite-models__excludePeople_true__id_34403964915__interactionViewName_photo-list-photo-interaction-view__isMobile_false__isOwner_false__layoutItem_1__model_1__modelParams_1__openAdvanced_false__parentContainer_1__parentSignature_photolist-561__requiredToShowOnClient_true__requiredToShowOnServer_true__rowHeightMod_1__searchSimilar_false__searchSimilarWithTerm_false__searchTerm_clearweather__searchType_1__showAdvanced_true__showInteractionBarPlaceholder_false__showSort_true__showTools_true__sortMenuItems_1__unifiedSubviewParams_1__viewType_jst" style="transform: translate(332px, 1018px); -webkit-transform: translate(332px, 1018px); -ms-transform: translate(332px, 1018px); width: 327px; height: 218px; background-image: url(//live.staticflickr.com/4169/34403964915_67b0d26e05_w.jpg)">
        <div class="interaction-view"></div>
        </div>
        '''
        if class_attribute and 'photo-list-photo-view' in class_attribute:
            style_attrs = item.attrs['style']
            if style_attrs:
                photo_url = style_attrs.split("//")[1]
                photo_url = photo_url[:-1]
                if count == 0:
                    return photo_url
                count = count - 1
    
    # Control should never reach here ideally
    # throw a print error along with returning a None, which is handled by the caller
    return None



if __name__=="__main__":
    print(get_image_url_from_flickr("CLEAR"))
