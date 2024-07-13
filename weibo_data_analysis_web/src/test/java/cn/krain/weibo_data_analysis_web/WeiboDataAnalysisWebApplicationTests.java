package cn.krain.weibo_data_analysis_web;

import cn.krain.weibo_data_analysis_web.util.DataTimeUtil;
import cn.krain.weibo_data_analysis_web.util.MenuMapping;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

@SpringBootTest
class WeiboDataAnalysisWebApplicationTests {

    @Test
    void contextLoads() {
        String password = "123456";
        try {
            MessageDigest digest = MessageDigest.getInstance("md5");
            byte[] result = digest.digest(password.getBytes());
            StringBuffer buffer = new StringBuffer();
            for (byte b : result) {
                //与运算
                int number = b & 0xff;  //加盐加密
                String str = Integer.toHexString(number);
                if (str.length() == 1) {
                    buffer.append("0");
                }
                buffer.append(str);
            }
            //标准的md5加密后的结果
            System.out.println(buffer.toString());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            System.out.println("");;
        }

    }

    @Test
    void Test01(){
        System.out.println(DataTimeUtil.getSysTime());
    }

    @Test
    void Test02(){
        String auth = "";
        String[] menus = {"热点话题","情感分析","舆情检索","系统配置"};
        for (int i = 0; i < menus.length; i++) {
            auth += MenuMapping.MENU_VALUE.get(menus[i]);
            if (i != menus.length-1)
                auth += "/";
        }
        System.out.println("auth: " + auth);
    }
}
