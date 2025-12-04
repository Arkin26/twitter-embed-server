from flask import Flask, request, Response, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<!-- REQUIRED FOR DISCORD -->
<meta property="og:site_name" content="Ahazek Embed">
<meta property="og:title" content="{{ title }}">
<meta property="og:description" content="{{ text[:200] }}">

<!-- IMPORTANT: URL OF THIS PAGE -->
<meta property="og:url" content="{{ request.url }}">

<!-- FOR IMAGE THUMBNAIL -->
{% if image_url %}
<meta property="og:image" content="{{ image_url }}">
<meta name="twitter:image" content="{{ image_url }}">
{% endif %}

<!-- FOR VIDEO -->
{% if video_url %}
<meta property="og:type" content="video.other">
<meta property="og:video" content="{{ video_url }}">
<meta property="og:video:url" content="{{ video_url }}">
<meta property="og:video:secure_url" content="{{ video_url }}">
<meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="720">
<meta property="og:video:height" content="1280">

<!-- REQUIRED FOR DISCORD VIDEO -->
<meta name="twitter:card" content="player">
<meta name="twitter:player" content="{{ video_url }}">
<meta name="twitter:player:width" content="720">
<meta name="twitter:player:height" content="1280">
{% endif %}

<title>{{ title }}</title>

<style>
body {
  background: #0f1419;
  color: #fff;
  font-family: Arial, sans-serif;
  padding: 20px;
}
.container {
  max-width: 600px;
  margin: auto;
  background: #1a1d21;
  padding: 20px;
  border-radius: 14px;
}
video, img {
  width: 100%;
  border-radius: 10px;
}
</style>

</head>
<body>

<div class="container">
  <h2>{{ title }}</h2>
  <p>{{ text }}</p>

  {% if video_url %}
  <video controls playsinline preload="none">
    <source src="{{ video_url }}" type="video/mp4">
  </video>
  {% elif image_url %}
  <img src="{{ image_url }}">
  {% endif %}
</div>

</body>
</html>
"""

@app.route("/")
def embed():
    title = request.args.get("title", "Tweet")
    name = request.args.get("name", "")
    handle = request.args.get("handle", "")
    text = request.args.get("text", "")
    image_url = request.args.get("image")
    video_url = request.args.get("video")

    return (
        render_template_string(
            HTML_TEMPLATE,
            title=title,
            text=text,
            image_url=image_url,
            video_url=video_url,
            request=request
        ),
        200,
        {"Content-Type": "text/html"}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
