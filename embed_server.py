from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">

    <!-- REQUIRED FOR DISCORD TO UNFURL -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#1d9bf0">

    <!-- GENERAL OG TAGS -->
    <meta property="og:title" content="{{ title }}">
    <meta property="og:description" content="{{ text[:200] }}">

    {% if image_url %}
    <meta property="og:image" content="{{ image_url }}">
    <meta name="twitter:image" content="{{ image_url }}">
    {% endif %}

    {% if video_url %}
    <meta property="og:type" content="video.other">
    <meta property="og:video" content="{{ video_url }}">
    <meta property="og:video:url" content="{{ video_url }}">
    <meta property="og:video:secure_url" content="{{ video_url }}">
    <meta property="og:video:type" content="video/mp4">
    <meta property="og:video:width" content="720">
    <meta property="og:video:height" content="1280">
    {% endif %}



    <title>{{ title }}</title>

    <style>
        body {
            background: #0f1419;
            color: #e7e9ea;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #192734;
            border-radius: 16px;
            padding: 16px;
            border: 1px solid #38444d;
        }
        .name { font-weight: 700; font-size: 16px; }
        .handle { color: #8899a6; font-size: 14px; margin-bottom: 10px; }

        .text {
            font-size: 20px;
            line-height: 1.35;
            white-space: pre-wrap;
            margin-bottom: 14px;
        }

        .media-container {
            margin-top: 14px;
            border-radius: 12px;
            overflow: hidden;
            background: #000;
        }
        video, img {
            width: 100%;
            height: auto;
            display: block;
        }

        .metrics {
            display: flex;
            gap: 16px;
            margin-top: 14px;
            padding-top: 14px;
            border-top: 1px solid #38444d;
            color: #8899a6;
            font-size: 14px;
        }
        .metric { display: flex; gap: 6px; align-items: center; }
    </style>
</head>

<body>
    <div class="container">
        <div class="name">{{ name }}</div>
        <div class="handle">@{{ handle }}</div>

        <div class="text">{{ text }}</div>

        {% if video_url %}
        <div class="media-container">
            <video controls playsinline preload="none">
                <source src="{{ video_url }}" type="video/mp4">
            </video>
        </div>
        {% elif image_url %}
        <div class="media-container">
            <img src="{{ image_url }}">
        </div>
        {% endif %}

        <div class="metrics">
            <div class="metric">💬 <strong>{{ replies }}</strong></div>
            <div class="metric">🔄 <strong>{{ retweets }}</strong></div>
            <div class="metric">❤️ <strong>{{ likes }}</strong></div>
            <div class="metric">👁️ <strong>{{ views }}</strong></div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def tweet_embed():

    title = request.args.get("title", "Tweet")
    name = request.args.get("name", "User")
    handle = request.args.get("handle", "user")
    text = request.args.get("text", "")

    video_url = request.args.get("video")
    image_url = request.args.get("image")

    likes = request.args.get("likes", 0)
    retweets = request.args.get("retweets", 0)
    replies = request.args.get("replies", 0)
    views = request.args.get("views", 0)

    return render_template_string(
        HTML_TEMPLATE,
        title=title,
        name=name,
        handle=handle,
        text=text,
        video_url=video_url,
        image_url=image_url,
        likes=likes,
        retweets=retweets,
        replies=replies,
        views=views,
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
