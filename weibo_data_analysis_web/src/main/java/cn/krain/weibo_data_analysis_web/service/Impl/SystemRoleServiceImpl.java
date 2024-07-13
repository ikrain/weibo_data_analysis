package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemRoleDao;
import cn.krain.weibo_data_analysis_web.entity.SystemRole;
import cn.krain.weibo_data_analysis_web.service.SystemRoleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author cc
 * @data 2022/5/9 - 16:07
 */
@Service
public class SystemRoleServiceImpl implements SystemRoleService {

    @Autowired
    private SystemRoleDao systemRoleDao;

    @Override
    public List<SystemRole> getAllRole(String rolename) {
        List<SystemRole> roleList = systemRoleDao.selectRole(rolename);
        return roleList;
    }

    @Override
    public void delRoleById(String id) {
        systemRoleDao.deleteRoleById(id);
    }

    @Override
    public void modifySystemRole(SystemRole systemRole) {
        systemRoleDao.updateRoleById(systemRole);
    }

    @Override
    public void addSystemRole(SystemRole systemRole) {
        systemRoleDao.insertRole(systemRole);
    }
}
