from blog.models import Post
import os
import frontmatter
from datetime import datetime

folder = '/users/ckelley/personal-site/nextjs-blog/posts'

file_list = os.listdir(folder)

parsed_posts = []

for file in file_list:

# file = file_list[0]
    dir = folder + '/' + file
    post = frontmatter.load(dir)
    title = post['title']
    created_on = datetime.strptime(post['date'], '%Y-%m-%d')
    updated_on = created_on
    status = 1
    slug = file.replace('.md','')
    content = post.content
    parsed_post = {
        'title': title,
        'slug': slug,
        'created_on': created_on,
        'updated_on': updated_on,
        'status': status,
        'content': content,
    }
    created_post = Post.objects.create(**parsed_post)
    created_post.save()
    parsed_posts.append(created_post)

