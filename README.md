# letsTagIt





**Professor:** Dr. Sambit Sahu

**Students:** Diksha Chouhan(dc4454), Manan Chawda(mrc9419), Aditya Chavan(ac8586), Shardha Koul (sk9225) 

**TAs:** Changhan Xie, Naga Bodepudi, Ruinan Zhang and Rahul Barhate




## Abstract
### Description: Hashtag Recommendation System that takes an image as input from the user, detects the objects present, and gives a list of relevant hashtags based on the input. Once the objects are detected, our system would search and filter trending hashtags on various social media platforms such as Twitter, Instagram, etc., using their APIs and generate a list of hashtags related to the content in the input image.

## Motivation (What problem are you trying to solve): 
To help social media influencers, brands, organizations in running their social media campaigns effectively. This could be an organic marketing tool that marketers use while running their campaigns.
 
One potential user of this application would be Brands that promote their products/services on social media. Brands often post images related to their products, services, promotions, etc. on these social media platforms. While posting images they are on the hunt for trending hashtags related to the image. So for users like those our app would make their job easier. Say if a brand wants to post a promotional discount offer during daughter’s day on their social media account our system would show a list of trending hashtags related to that image during that time.

The trigger could also be a text input, not necessarily an image. As per our current idea, once we get the input image we plan to pass it through an object detection algorithm. This algorithm would potentially create a list of objects found in the image. Suppose if the image is of a girl holding a gift in her hand the algorithm should give out a list that looks like [girl, gift]. We still need to explore the libraries that we would have to use for this detection part. Once we have this list we would make rest calls to the APIs provided by these social media platforms and pass the objects of this list as input one by one to get the list of trending hashtags.

Thus for the above input, an image of a girl holding a gift during daughter’s day the output from our system should ideally give trending hashtags related to daughter’s day.

Further down the line, we can include some analysis related to each hashtag that is being recommended. Data like the number of posts, popularity of the tag by location, reach, etc could be added.

