## Jason Davis
## playing with planetlabs api satellite imagery
## 16 February 2016
library(raster)
setwd("/home/jasondavis/planet_api/")
a <- list.files('output')
length(a)
file <- paste("output", a[1], sep="/")

b <- raster(file)
plot(b)
