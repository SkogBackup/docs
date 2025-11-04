## 1) Input Variable

[Inputs]
{{$XML_CONTENT}}
[/Inputs]

## 2) Instructions Structure

[Instructions Structure]

1. Begin with an explanation of the task: converting XML syntax to square bracket syntax
2. Present the XML content to be converted ({$XML_CONTENT})
3. Provide detailed conversion rules
4. Give examples of specific conversions
5. Instruct to process the entire document maintaining structure and semantics
6. Request the output in specified format
[/Instructions Structure]

## 3) Final Instructions

[Instructions]

# XML to Square Bracket Syntax Converter

You will convert XML-style content to a custom square bracket syntax. The input will be content that uses XML tags, and you'll transform it following specific conversion rules while maintaining the original structure and meaning.

[xml_content]
{{$XML_CONTENT}}
[/xml_content]

## Conversion Rules

Follow these rules to convert the XML syntax to square bracket syntax:

1. **Basic Tag Conversion**:
   - Change `<tag>` to `[tag]`
   - Change `</tag>` to `[/tag]`

2. **Attributes Conversion**:
   - Transform `<tag attr="value">` to `[tag:attr$value]`
   - For multiple attributes: `<tag attr1="val1" attr2="val2">` becomes `[tag:attr1$val1:attr2$val2]`

3. **Special XML Elements**:
   - XML declarations: `<?xml version="1.0"?>` → `[!xml:version$1.0]`
   - CDATA sections: `<![CDATA[...]]>` → `[!cdata[...]]`
   - Comments: `<!-- comment -->` → `[!-- comment --]`
   - Self-closing tags: `<tag />` → `[tag/]`
   - Entity references: `&entity;` → `@entity@`

## Examples of Specific Conversions

- `<person>John</person>` → `[person]John[/person]`
- `<book title="The Great Gatsby">` → `[book:title$The Great Gatsby]`
- `<img src="photo.jpg" alt="Profile" />` → `[img:src$photo.jpg:alt$Profile/]`
- `<!-- Note: Important -->` → `[!-- Note: Important --]`
- `<p>Copyright &copy; 2023</p>` → `[p]Copyright @copy@ 2023[/p]`

## Processing Instructions

1. Process the entire document systematically, converting all XML elements to the square bracket syntax.
2. Maintain the document's structure, hierarchy, and indentation.
3. Preserve all text content exactly as it appears in the original.
4. Be particularly careful with nested tags and ensure proper conversion of opening and closing tags.
5. Ensure all attributes are properly converted with the colon and dollar sign notation.

[scratchpad]
Use this space to work through complex conversion challenges. For each challenging element:

1. Identify the XML pattern
2. Determine the correct square bracket equivalent
3. Apply the conversion rules consistently
[/scratchpad]

Present your complete converted document inside [converted_content] tags. The converted content should maintain the same structure, spacing, and line breaks as the original XML document.
[/Instructions]
