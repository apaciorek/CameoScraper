df <- read.csv("cameo_data.csv", header = FALSE)
df
View(df)
df <- read.csv("cameo_data.csv", header = FALSE)
names(df)
length(V1)
length(df$V1)
length(unique(df$V1))
cameo_df = read.csv("talent_data.csv", header = FALSE, stringsAsFactors = FALSE)
length(unique(cameo_df$V1))
cam2 <- distinct(cameo_df, V1, .keep_all = TRUE)
View(cam2)
cam2$V2 = str_remove(cam2$V2, "Book now for \\$")
cam2$V2 = as.numeric(gsub(',', '', cam2$V2))
cam2$V6 = as.numeric(str_remove(cam2$V6, " stars"))
cam2$V5 = str_remove(str_remove(cam2$V5, " Reviews"), " Review")
cam2[907, "V5"] <- "8"
cam2[748, "V5"] <- "6"
filter(cam2, cam2$V5 == "Reviews")
cam2$V5 = as.numeric(cam2$V5)
url_parse(cam2$V7)
test = "['https://www.cameo.com/c/broadway', 'https://www.cameo.com/c/actors', 'https://www.cameo.com/c/hamilton']"
head(cam2)
class(cam2$V7)
class(test)
str_remove_all(str_remove_all(test, "\\["), "\\]")
url_parse(str_remove_all(str_remove_all(str_remove_all(cam2$V7, "\\["), "\\]"), "\\'"))
test2 = cam2[1,"V7"]
test2
test2 = str_remove_all(str_remove_all(str_remove_all(test2, "\\["), "\\]"), "\\'")
test2
test2 = url_parse(unlist(strsplit(test2, ", ")))$path
test2
camcopy = cam2
for (x in camcopy$V7) {
  str_remove_all(str_remove_all(str_remove_all(x, "\\["), "\\]"), "\\'")
  print(x)
}
View(camcopy)
test3 = camcopy$V7[1]
test3 = str_remove_all(str_remove_all(str_remove_all(test3, "\\["), "\\]"), "\\'")
test3 = url_parse(unlist(strsplit(test3, ", ")))$path
test3
obs = nrow(camcopy)
class(obs)
obs
for (i in 1:obs){
  camcopy$V7[i] = str_remove_all(str_remove_all(str_remove_all(camcopy$V7[i], "\\["), "\\]"), "\\'")
}
for (i in 1:obs){
  camcopy$V7[i] = url_parse(unlist(strsplit(camcopy$V7[i], ", ")))$path
}
class(camcopy$V7)
copy2 = camcopy
copy2$V7 = str_remove(copy2$V7, "c\\/")
View(copy2)
