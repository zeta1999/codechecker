# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------


from codechecker_report_converter.analyzer_result import AnalyzerResult
from codechecker_report_converter.plist_converter import PlistConverter

from .output_parser import TSANParser


class TSANAnalyzerResult(AnalyzerResult):
    """ Transform analyzer result of Clang ThreadSanitizer. """

    TOOL_NAME = 'tsan'
    NAME = 'ThreadSanitizer'
    URL = 'https://clang.llvm.org/docs/ThreadSanitizer.html'

    def parse(self, analyzer_result):
        """ Creates plist files from the given analyzer result to the given
        output directory.
        """
        parser = TSANParser()

        content = self._get_analyzer_result_file_content(analyzer_result)
        if not content:
            return

        messages = parser.parse_messages(content)

        plist_converter = PlistConverter(self.TOOL_NAME)
        plist_converter.add_messages(messages)
        return plist_converter.get_plist_results()
