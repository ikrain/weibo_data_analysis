package cn.krain.weibo_data_analysis_web.dao;

import cn.krain.weibo_data_analysis_web.entity.SystemUser;
import cn.krain.weibo_data_analysis_web.vo.SystemUserVo;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;
import java.util.Map;

/**
 * @author cc
 * @data 2022/5/5 - 22:54
 */
public interface SystemUserDao {
    /**
     * 用户登录
     * @param map   map中包含用户名和密码
     * @return
     */
    SystemUser selectLoginUser(Map<String, String> map);

    /**
     * 通过token获取用户信息
     * @param token
     * @return
     */
    SystemUser selectUserByToken(String token);

    /**
     * 获取所有用户
     * @return
     */
    List<SystemUser> getUser(String username);

    void deleteUserById(String id);

    void insertUser(SystemUser systemUser);

    void updateUser(SystemUser systemUser);

    /**
     * 分页查询
     * @param map
     * @return
     */
    List<SystemUser> getPageUser(Map<String, Object> map);

    int selectUserNum();

    /**
     * 多表查询，重新封装前端所需要的数据
     * @return
     */
    SystemUserVo selectUserVoByToken(String token);
}
