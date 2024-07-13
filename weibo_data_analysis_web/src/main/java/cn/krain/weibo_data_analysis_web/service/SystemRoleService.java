package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.entity.SystemRole;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemRoleService {
    List<SystemRole> getAllRole(String rolename);

    void delRoleById(String id);

    void modifySystemRole(SystemRole systemRole);

    void addSystemRole(SystemRole systemRole);
}
