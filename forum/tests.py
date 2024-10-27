from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Forum, Reply

class ForumTests(TestCase):

    def setUp(self):
        # Set up user and client
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        # Set up sample forum data
        self.forum = Forum.objects.create(
            title="Sample Forum",
            description="Sample description",
            created_by=self.user
        )

    def test_show_forum(self):
        response = self.client.get(reverse('forum:show_forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum.html')
        self.assertContains(response, "Sample Forum")

    def test_create_forum(self):
        response = self.client.post(reverse('forum:create_forum'), {
            'title': 'New Forum Title',
            'description': 'New Forum Description',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creating forum
        self.assertEqual(Forum.objects.count(), 2)  # One initial + one new forum
        self.assertTrue(Forum.objects.filter(title="New Forum Title").exists())

    def test_submit_forum_valid_data(self):
        response = self.client.post(reverse('forum:submit_forum'), {
            'title': 'Submitted Forum',
            'description': 'This is a submitted forum description'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertTrue(Forum.objects.filter(title="Submitted Forum").exists())

    def test_submit_forum_invalid_data(self):
        response = self.client.post(reverse('forum:submit_forum'), {
            'title': '',
            'description': 'Description without title'
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': False, 'message': 'Invalid data'})

    def test_delete_forum(self):
        response = self.client.post(reverse('forum:delete_forum', args=[self.forum.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertFalse(Forum.objects.filter(id=self.forum.id).exists())

    def test_reply_forum_valid(self):
        response = self.client.post(reverse('forum:reply_forum', args=[self.forum.id]), {
            'content': 'This is a reply content'
        })
        self.assertEqual(response.status_code, 200)
        reply_data = response.json().get('reply')
        self.assertEqual(reply_data['content'], 'This is a reply content')
        self.assertEqual(reply_data['username'], 'testuser')
        self.assertTrue(Reply.objects.filter(content="This is a reply content").exists())

    def test_reply_forum_invalid(self):
        response = self.client.post(reverse('forum:reply_forum', args=[self.forum.id]), {
            'content': ''
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'error': 'Content is required'})

    def test_delete_reply(self):
        reply = Reply.objects.create(
            forum=self.forum,
            content="Reply to be deleted",
            created_by=self.user
        )
        response = self.client.post(reverse('forum:delete_reply', args=[reply.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertFalse(Reply.objects.filter(id=reply.id).exists())
