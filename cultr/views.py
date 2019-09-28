from django.views.generic import TemplateView


class HomeView(TemplateView):

    # all html files are not name spaced just for fast prototyping
    template_name = 'index.html'

class TermsOfUseView(TemplateView):

    template_name = 'terms_of_use.html'

class PrivacyPolicyView(TemplateView):

    template_name = 'privacy_policy.html'

