require 'rack/offline'

set :css_dir, 'stylesheets'

set :js_dir, 'javascripts'

set :images_dir, 'images'

offline = Rack::Offline.configure do
  cache "stylesheets/aqplot.css"
  cache "images/ah.jpg"
  cache "images/dial.png"
  cache "images/glyphicons-halflings-white.png"
  cache "images/glyphicons-halflings.png"
  cache "images/horizon.png"
  cache "javascripts/all.js"
end

map("/offline.appcache") { run offline }
# We need to add this page declaration to force middleman to include the manifest in a build
page "/offline.appcache", :proxy => "offline.appcache"

page "/" do 
  @active = "index"
end
page "/dashboard.html" do 
  @active = "dashboard"
end
page "/sensors.html" do 
  @active = "sensors"
end
page "/receiver.html" do 
  @active = "receiver"
end
page "/engines.html" do 
  @active = "engines"
end

# Build-specific configuration
configure :build do
  # For example, change the Compass output style for deployment
  activate :minify_css
  
  # Minify Javascript on build
  # activate :minify_javascript
  
  # Enable cache buster
  # activate :cache_buster
  
  # Use relative URLs
  activate :relative_assets
  
  # Compress PNGs after build
  # First: gem install middleman-smusher
  # require "middleman-smusher"
  # activate :smusher
  
  # Or use a different image path
  # set :http_path, "/Content/images/"
end