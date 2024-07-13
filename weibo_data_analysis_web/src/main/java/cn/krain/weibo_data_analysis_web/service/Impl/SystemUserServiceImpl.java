package cn.krain.weibo_data_analysis_web.service.Impl;

import cn.krain.weibo_data_analysis_web.dao.SystemUserDao;
import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.service.SystemUserService;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 23:19
 */
@Service
public class SystemUserServiceImpl implements SystemUserService {

    @Autowired
    private SystemUserDao systemUserDao;

    @Override
    public SystemUser userLogin(Map<String, String> map) {
        SystemUser systemUser = systemUserDao.selectLoginUser(map);
        return systemUser;
    }

    @Override
    public SystemUser getUserByToken(String token) {
        SystemUser systemUser = systemUserDao.selectUserByToken(token);
        return systemUser;
    }

    @Override
    public List<SystemUser> getAllUser(String username) {
        List<SystemUser> userList = systemUserDao.getUser(username);
        return userList;
    }

    @Override
    public List<SystemUser> getAllPageUser(Map<String, Object> map) {
        List<SystemUser> userList = systemUserDao.getPageUser(map);
        return userList;
    }

    @Override
    public void delUserById(String id) {
        systemUserDao.deleteUserById(id);
    }

    @Override
    public void addSystemUser(SystemUser systemUser) {
        systemUserDao.insertUser(systemUser);
    }

    @Override
    public void modifySystemUser(SystemUser systemUser) {
        systemUserDao.updateUser(systemUser);
    }

    @Override
    public int queryUserNum() {
        return systemUserDao.selectUserNum();
    }

    @Override
    public SystemUserVo getUserVoByToken(String token) {
        return systemUserDao.selectUserVoByToken(token);
    }
}
