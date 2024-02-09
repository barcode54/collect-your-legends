# Collect your legends bot

this bot is really cool

## Usage
### Commands:
`/start` - starts the bot
`/harem` - shows **harem**
`/gift <id>` - gift a champion you have by replying to another user message (you need to know your champ id (you can check your harem) )
`/profile` - show your **profile** -> soon you will be able to set a custom pfp and username for the bot
`/shop` - *coming soon*
`/coins` - view your **coins** -> currently no use but its cool to have coins

enjoy plz


## Documentation (do not read)
 
### MongoDB structure

    {
    	"_id": "1",
    	"name": "Aatrox",
    	"skinline": "base",
    	"role": "top",
    	"image": "images/aatrox.png",
    	"sauce": "https://wallpapersden.com/aatrox-legends-of-runeterra-wallpaper/768x1024/",
    	"guesses": ["Aatrox"]
    }

*nb guesses is the criteria used for the protecc*
<hr>


### Classes


**Legend:**
  

    class Legend:
	  def __init__(self, _id, name, skinline, role, image, sauce, guesses):
		  self._id = _id
		  self.name = name
		  self.skinline = skinline	 
		  self.role = role
		  self.image = image
		  self.sauce = sauce
		  self.guesses = guesses

**User**:

    class User:
      def __init__(self, id, name, date, harem, coins, count, unique, level, xp):
	      self.id = id
	      self.name = name
	      self.date = get_date()
	      self.harem = harem
	      self.count = count
	      self.unique = unique
	      self.coins = coins
	      self.level = level
	      self.xp = xp
	      
	      def get_completion_rate(self):

**Group**

    class Group:
      def __init__(self, title, photo):
	        self.title = title
	        self.photo = photo
    
      def get_top_users(self):

<hr>

### Methods
**General**

    def get_date(): //da fare

**Database**

    def legendObj(legend):
    def get_legend_by_id(id):
    def get_all_legends():
    def get_legends_by_role(role):
    def get_legends_by_skinline(skinline):
    def get_legends_by_name(name):
    def get_legends_by_regex(regex):
    def add_legend(legend): // da fare
