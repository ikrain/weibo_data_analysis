package cn.krain.weibo_data_analysis_web.util;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * @author CC
 * @data 2020/12/15 - 16:54
 */
public class MD5Util {

    public static String getMD5(String password) {
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
            return buffer.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return "";
        }
    }

}
