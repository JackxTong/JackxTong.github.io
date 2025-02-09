

>
## My personal webpage

### Forked from [Qiu Baiying](http://qiubaiying.github.io)


With Jekyll, need to run `jekyll serve`, then can view the website in real time from local at `http://127.0.0.1:4000/`

###
To create more buttons parallel to 'home' or 'experience', create html in the root directory.

Need to have
```
---
layout: page
title: ""
lang: "en"
header-img: "img/black_image_2000x1000.jpg"
---
```

In `notes.html`, when I do
```
{% for post in site.posts %}{% if post.label == 'notes' %}
```

`_layouts/post.html` is responsible for taking markdown posts from `_posts/`, put them in `_site` classified under the markdown posts' dates, meanwhile
dynamically modifying `_site/2025/../note/index.html`


## License

[LICENSE](https://github.com/qiubaiying/qiubaiying.github.io/blob/master/LICENSE)。

