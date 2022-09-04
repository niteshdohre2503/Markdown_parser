import unittest
import md_to_html

class TestCalc(unittest.TestCase):

    def test_h1(self):
        self.assertEqual(md_to_html.reg("# Head1"), "<h1>Head1</h1>")
        self.assertEqual(md_to_html.reg("# SomefirstHeading"), "<h1>SomefirstHeading</h1>")
    
    def test_h2(self):
        self.assertEqual(md_to_html.reg("## Heading is 2"), "<h2>Heading is 2</h2>")
        self.assertEqual(md_to_html.reg("## SomeText"), "<h2>SomeText</h2>")

    def test_bold(self):
        self.assertEqual(md_to_html.reg("**Heading is 2**"), "<b>Heading is 2</b>")
        self.assertEqual(md_to_html.reg("**SomeText**"), "<b>SomeText</b>")

    def test_italic(self):
        self.assertEqual(md_to_html.reg("*Heading is 2*"), "<em>Heading is 2</em>")
        self.assertEqual(md_to_html.reg("*SomeText*"), "<em>SomeText</em>")



    
if __name__ == '__main__':
    unittest.main()