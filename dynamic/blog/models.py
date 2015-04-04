from django.db import models
import website.models


# Blog articles
class BlogArticleItem(website.models.BaseItem):
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=100)
    markdown_content = models.TextField(blank=True)
    html_content = models.TextField(blank=True)
    is_shown = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s:%s" % (self.id, self.title)


# Comments
class BlogCommentItem(website.models.BaseItem):
    article = models.ForeignKey(BlogArticleItem, null=False, related_name="comments")
    content = models.TextField(blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.id, self.related_article_id)
