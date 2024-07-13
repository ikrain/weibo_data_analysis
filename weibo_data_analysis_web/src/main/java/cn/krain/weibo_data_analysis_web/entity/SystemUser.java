package cn.krain.weibo_data_analysis_web.entity;

import lombok.Data;
import java.io.Serializable;

/**
 * @author cc
 * @data 2022/5/5 - 22:55
 */
@Data
public class SystemUser implements Serializable {
    private String id;
    private String username;
    private String password;
    private String role_id;
    private String token;
    private String role_name;
    private String avatar;
    private String create_time;
}
