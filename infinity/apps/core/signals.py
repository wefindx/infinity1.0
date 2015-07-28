def _comment_post_save(sender, instance, created, *args, **kwargs):
    """
    After the user save comment, send e-mail notifications
    """
    from users.models import User
    from constance import config
    from os import path
    from re import finditer

    subject_template_path='mail/comments/mention_notification_subject.txt'
    email_template_path='mail/comments/mention_notification.html'

    comment = instance.text
    usernames = [m.group(1) for m in finditer('\[([^]]+)\]', comment)]
    usernames = usernames[:config.MAX_MENTIONS_PER_COMMENT]

    users = User.objects.filter(username__in=usernames)

    if users.exists():

        url = "%s/%s/detail/#" % (instance.content_type,
                                  instance.content_object.id)
        link = path.join(instance.content_object.get_absolute_url(), url)

        from .utils import send_mail_template

        for user in users.iterator():

            send_mail_template(subject_template_path,
                                email_template_path,
                                recipient_list=[user.email],
                                context={'user': instance.user.username,
                                         'comment': instance.text,
                                         'link': link})
