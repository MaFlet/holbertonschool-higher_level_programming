#!/usr/bin/python3
"""
Script that serialize and deserialize via XML
as alternative format to JSON
"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=dangerous-default-value
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        item.set("Key", str(key))
        item.text = str(value)
        item.set("type", type(value).__name__)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for item in root.findall("item"):
        key = item.get("Key")
        value = item.text
        value_type = item.get("type")

        if value_type == "int":
            value = int(value)
        elif value_type == "float":
            value = float(value)
        elif value_type == "bool":
            value = value.lower() == "true"

        result[key] = value

    return result
