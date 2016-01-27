from zope.publisher.browser import BrowserView
from plone import api
from lxml import html


class SectionMeny(BrowserView):
    def __call__(self):
        section = self.request.get("section", None)
        if section is None:
            return
        portal = api.portal.get()
        section = portal.get(section,None)
        if section is None:
            return
        section_menu = section.get("section-menu",None)
        if section_menu is None:
            return
        try:
            ret = html.fromstring(section_menu()).get_element_by_id("content")
        except KeyError:
            return
        return '<div class="container sectionsubmenu %s">%s</div>' % (section.getId(), html.tostring(ret))
