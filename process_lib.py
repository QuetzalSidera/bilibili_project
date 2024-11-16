# 检查标题本身是否含有编号，取未编号的部分 以防交互界面二次编号
# 逻辑：若所有标题第一位都是数字，则视为标题中带有编号，删除数字，从非符号位开始取到最后一个
def remove_index(unprocessed_title_list):
    is_title_with_index = 0
    chinese_index_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    num_index_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    separator_list = ["\0", "\t", " ", ",", "、", "."]
    remove_item = "".join(chinese_index_list + num_index_list + separator_list)
    for title in unprocessed_title_list:
        if title[0] in chinese_index_list or num_index_list:
            is_title_with_index = 1
        else:
            is_title_with_index = 0
            break
    if is_title_with_index == 1:  # 如果标题带有编号
        for i in range(len(unprocessed_title_list)):
            unprocessed_title_list[i] = unprocessed_title_list[i].lstrip(remove_item)
    return unprocessed_title_list
