package cn.krain.weibo_data_analysis_web.util;

import java.util.HashMap;
import java.util.Map;

/**
 * @author CC
 * @data 2020/12/16 - 19:43
 */
public class MenuMapping {

    /**
     * 用户权限：系统中文模块对应路径
     */

    public static String TOPIC = "Topic";

    public static String EMOTION = "Emotion";

    public static String SEARCH = "Search";

    public static String MANAGE = "Manage";

    public static String USER = "User";

    public static String ROLE = "Role";

    public static String MENU = "Menu";

    public static String SET = "Set";

    public static Map<String, String> MENU_VALUE = new HashMap<>();

    static {
        MENU_VALUE.put("热点话题", TOPIC);
        MENU_VALUE.put("情感分析", EMOTION);
        MENU_VALUE.put("舆情检索", SEARCH);
        MENU_VALUE.put("系统管理", MANAGE);
        MENU_VALUE.put("用户管理", USER);
        MENU_VALUE.put("角色权限管理", ROLE);
        MENU_VALUE.put("系统配置", SET);
    }

}
