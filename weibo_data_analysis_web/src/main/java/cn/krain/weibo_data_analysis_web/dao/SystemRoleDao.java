package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemRole;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemRoleDao {

    List<SystemRole> selectRole(String rolename);

    void deleteRoleById(String id);

    void updateRoleById(SystemRole systemRole);

    void insertRole(SystemRole systemRole);
}
