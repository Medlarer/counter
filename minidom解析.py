from xml.dom import minidom

with open("dom_write.xml","r",encoding="utf-8") as f:
    # parse()获取DOM对象
    dom = minidom.parse(f)
    # 获取根节点
    root = dom.documentElement
    # 节点名称
    print(root.nodeName)
    # 节点类型："ELEMENT_NODE",元素节点；"TEXT_NODE"，文本节点；"ATTRIBUTE_NODE"，属性节点
    print(root.nodeType)
    # 获取某个节点下所有子节点，列表
    print(root.childNodes)
    #通过dom对象或根元素，再根据标签名获取元素节点，是个列表
    book = root.getElementsByTagName("book")[0]
    # 获取节点属性
    print(book.getAttribute("price"))
    # 获取某个元素节点的文本内容，先获取子文本节点，然后通过"data"属性获取文本内容
    name = root.getElementsByTagName("name")[0]
    name_text_node = name.childNodes[0]
    print(name_text_node.data)
    #获取某节点的父节点
    print(name.parentNode.nodeName)