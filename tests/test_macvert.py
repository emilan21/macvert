import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from macvert.mac_operations import Operations


FORMATS = {
    "colon": "aa:bb:cc:dd:ee:ff",
    "hp": "aabb-ccdd-eeff",
    "no_delimiter": "aabbccddeeff",
    "dash": "aa-bb-cc-dd-ee-ff",
}


class ConverterTests(unittest.TestCase):
    def test_every_format_pair(self):
        for input_type, address in FORMATS.items():
            for output_type, expected in FORMATS.items():
                with self.subTest(input_type=input_type, output_type=output_type):
                    self.assertEqual(Operations(address, input_type, output_type).get_mac(), expected)

    def test_validation(self):
        for address in ("aa:bb:cc:dd:ee", "aa:bb:cc:dd:ee:gg", "aabb-ccdd-eee"):
            with self.subTest(address=address):
                with self.assertRaises(ValueError):
                    Operations(address, "colon", "hp").get_mac()
        with self.assertRaises(ValueError):
            Operations(FORMATS["colon"], "unknown", "hp").get_mac()
        with self.assertRaises(ValueError):
            Operations(FORMATS["colon"], "colon", "unknown").get_mac()

    def test_cli_file_and_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            address_file = Path(temp) / "addresses.txt"
            address_file.write_text("aa:bb:cc:dd:ee:ff\n\nAA:BB:CC:DD:EE:FF\n")
            command = [sys.executable, "-m", "macvert.cli", "cli", "-f", str(address_file), "-i", "colon", "-o", "hp"]
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), ["aabb-ccdd-eeff", "AABB-CCDD-EEFF"])
            invalid = subprocess.run(command[:4] + ["-m", "invalid", "-i", "colon", "-o", "hp"], capture_output=True, text=True, check=False)
            self.assertNotEqual(invalid.returncode, 0)

    def test_web_get_and_post(self):
        from macvert.web import app

        client = app.test_client()
        self.assertEqual(client.get("/").status_code, 200)
        response = client.post("/", data={"macs": FORMATS["colon"], "input_type": "colon", "output_type": "hp"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(FORMATS["hp"].encode(), response.data)


if __name__ == "__main__":
    unittest.main()
