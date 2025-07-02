"""
This plugin is used to set the scope of previous and next navigation buttons to the directory pages are located in.

The first page in a directory will have no previous button, and the last no next button.

NOTE: This is calculated based on the sorting order of the page file names within the directory.
Therefore custom ordering of pages using .nav.yml will cause unexpected results.
"""

from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page
from mkdocs.utils.templates import TemplateContext
from collections import defaultdict
import os


class ScopedNavPlugin(BasePlugin):
    """
    Extends the MkDocs BasePlugin to create the scoped nav plugin.
    """
    def on_nav(self, nav: Navigation, config, files) -> Navigation:
        """
        Modifies the global site navigation to sort by parent directory.

        Parameters:
            nav (Navigation): Navigation instance containing the pages.
            config: Global configuration.
            files: Global files collection.

        Returns:
            nav (Navigation): The modified Navigation instance.
        """
        # Group pages by parent directory
        self.page_groups = defaultdict(list)
        for page in nav.pages:
            dir_path = os.path.dirname(page.file.src_path)
            self.page_groups[dir_path].append(page)

        # Sort each group by the order in the nav
        for group in self.page_groups.values():
            # print("ScopedNavPlugin Group:")
            # for page in group:
            #     print(f"  - {page.file.src_path}")
            group.sort(key=lambda p: nav.pages.index(p))

        # Return the modified Navigation object
        return nav

    def on_page_context(self, context: TemplateContext, page: Page, config, nav: Navigation) -> TemplateContext:
        """
        Modifies the context of the Page object to set the previous/next button.

        If there is no previous page, set the previous_page attribute to None.
        If there is no next page, set the next_page attribute to None.

        Parameters:
            context (TemmplateContext): Instance of the TemplateContext to modify.
            page (Page): Page object to use for the context.
            config: Global configuration.
            nav (Navigation): Navigation instance.

        Returns:
            context (TemplateContext): Modified TemplateContext instance.
        """
        # print(f"ScopedNavPlugin processing: {page.file.src_path}")
        # Get the group this page is associated with
        dir_path = os.path.dirname(page.file.src_path)
        group = self.page_groups.get(dir_path, [])

        # Set previous and next index based on where they are in the group
        if page in group:
            idx = group.index(page)
            # Set to previous page if this isn't the first page, otherwise None
            context['previous_page'] = group[idx - 1] if idx > 0 else None
            # print(f"ScopedNavPlugin prev: {context.get('previous_page')}")
            # Set to next page if this isn't the last page, otherwise None
            context['next_page'] = group[idx + 1] if idx < len(group) - 1 else None
            # print(f"ScopedNavPlugin next: {context.get('next_page')}")

        return context
