package cn.krain.weibo_data_analysis_web.util;

import java.util.UUID;

public class UUIDUtil {
    public static String getUUID() {
        return UUID.randomUUID().toString().replaceAll("-", "");
    }
}
