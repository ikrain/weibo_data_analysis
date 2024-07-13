package cn.krain.weibo_data_analysis_web.service;

import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:56
 */
@Service
public interface SystemUserService {
    /**
     * 用户登录服务接口
     * @param map
     * @return
     */
    SystemUser userLogin(Map<String, String> map);

    /**
     * 通过token获取用户信息
     * @param token
     * @return
     */
    SystemUser getUserByToken(String token);

    List<SystemUser> getAllUser(String username);

    List<SystemUser> getAllPageUser(Map<String, Object> map);

    void delUserById(String id);

    void addSystemUser(SystemUser systemUser);

    void modifySystemUser(SystemUser systemUser);

    int queryUserNum();

    SystemUserVo getUserVoByToken(String token);
}
