class Settings:
	
	def __init__(self):
		self.screen_width = 1050
		self.screen_breadth = 800
		self.bg_color = [230,230,230]
		
		self.ship_limit = 3
		
		self.bullet_width = 3 
		self.bullet_height = 15
		self.bullet_color = 60,60,60

		self.bullets_allowed = 7

		self.fleet_drop_speed = 10
		
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 2.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
	# fleet direction 1 means right while -1 means left
		self.fleet_direction = 1
	# The above dynamic def is used for real time game update
	# it adds more logic

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale 


