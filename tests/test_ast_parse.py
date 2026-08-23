import unittest
import os
import subprocess
import json

class TestASTParse(unittest.TestCase):
    def parse_js_array_node(self, filepath, var_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, filepath).replace('\\', '/')
        node_script = f"""
        const fs = require('fs');
        const code = fs.readFileSync('{full_path}', 'utf8');
        eval(code.replace('const {var_name}', 'global.{var_name}'));
        console.log(JSON.stringify(global.{var_name}));
        """
        res = subprocess.run(['node', '-e', node_script], capture_output=True, text=True, encoding='utf-8', check=True)
        return json.loads(res.stdout)

    def test_parse_projects_and_certs(self):
        p = self.parse_js_array_node('js/projectsData.js', 'PROJECTS_DATA')
        c = self.parse_js_array_node('js/certificatesData.js', 'CERTIFICATES_DATA')
        self.assertGreater(len(p), 0, "PROJECTS_DATA should not be empty")
        self.assertGreater(len(c), 0, "CERTIFICATES_DATA should not be empty")

if __name__ == '__main__':
    unittest.main()


