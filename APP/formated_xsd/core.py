import xml.etree.ElementTree as ET


def remove_annotations(xsd_filepath, output_filepath):
    try:
        tree = ET.parse(xsd_filepath)

        for element in tree.iter():
            for child in list(element):
                if 'annotation' in child.tag:
                    element.remove(child)

        with open(output_filepath, 'wb') as f:
            tree.write(f, encoding='utf-8')

        return {"error": False, "text_error": ""}

    except Exception as e:
        return {"error": True, "text_error": f"Произошла ошибка чтения:\n{e}"}


if __name__ == '__main__':
    input_xsd_filename = input("Введите имя файла XML: ")
    input_xsd_filepath = f"{input_xsd_filename}.xml"
    output_xsd_filepath = f"{input_xsd_filename}_output.xml"
    remove_annotations(input_xsd_filepath, output_xsd_filepath)