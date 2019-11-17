---
layout: doc_page
title: Downloads
breadcrumb: Learn
toc: false
description: Get an introduction to the rules of the game to win the Halite AI Programming Challenge.
sort_key: 3
---

<div class="doc-section" markdown="1">



## STARTER KITS DOWNLOAD
Download a starter kit to start building your bot.


<div class="table-container">
    <table class="table">
        <thead>
            <tr>
                <td></td>
                <td></td>
                <th colspan="{{ site.data.downloads.platforms | size }}" class="text-center">Operating System</th>
            </tr>
            <tr>
                <th>Language</th>
                <td>Version</td>
                {% for platform in site.data.downloads.platforms %}
                <td>{{ platform }}</td>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for language in site.data.downloads.languages %}
            <tr>
                <td>{{ language.language }}</td>
                <td>{{ language.version }}</td>
                {% for file in language.files %}
                <td><a href="{{ site.baseurl }}/{{ file }}" onclick="javascript:handleOutboundLinkClicks('play', 'download','starter-kit');return true;">Download</a></td>
                {% endfor %}
            </tr>
            {% endfor %}
            <tr>
                <td>Only Game Engine</td>
                <td>{{ site.data.downloads.version }}</td>
                <td>NA</td>
                {% for file in site.data.downloads.environments %}
                <td><a href="{{ site.baseurl }}/{{ file }}" onclick="javascript:handleOutboundLinkClicks('play', 'download','starter-kit');return true;">Download</a></td>
                {% endfor %}
            </tr>
        </tbody>
    </table>
</div>
<br>
