from blog.models import Post
from blog.serializers import PostSerializer
import os
import frontmatter
from datetime import datetime
import pytz

'''
# DELETE ALL EXISTING POSTS #
from blog.models import Post
Post.objects.all().delete()
'''

folder = '/users/ckelley/personal-site/nextjs-blog/posts'

file_list = os.listdir(folder)

eastern = pytz.timezone('US/Eastern')

parsed_posts = []

for file in file_list:
    dir = folder + '/' + file
    post = frontmatter.load(dir)
    title = post['title']
    new_date = datetime.strptime(post['date'], '%Y-%m-%d').replace(tzinfo=eastern)
    created_on = new_date
    published_on = new_date
    status = 1
    slug = file.replace('.md','')
    content = post.content
    parsed_post = {
        'title': title,
        'slug': slug,
        'created_on': created_on,
        'published_on': published_on,
        'status': status,
        'content': content,
    }
    created_post = Post.objects.create(**parsed_post)
    created_post.save()
    post = Post.objects.get(slug=slug)
    serialized_post = PostSerializer(post).data
    print(serialized_post)
    parsed_posts.append(created_post)

