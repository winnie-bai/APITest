pipeline{
    agent {
        label 'Linux'
    }
    stages{
        stage('build env') {
            steps {
                 build 'main_job'
            }
        }
        stage('wait'){
            steps{
                waitUntil(initialRecurrencePeriod: 3000) {
                    script {
                        def r = sh script: 'curl http://www.baidu.com', returnStatus: true
                        return (r == 0)
                    }
                }
            }
        }
        stage('api_test') {
            steps('run test') {
                sh '''cd $WORKSPACE
                      python3 -m pip install -r requirements.txt
                      python3 run.py'''
            }
            steps('generate report'){
                allure includeProperties: false, jdk: '', results: [[path: '$WORKSPACE/allure-results']]
            }
            steps('archiveArtifacts'){
                archiveArtifacts artifacts: 'logs/*', followSymlinks: false
            }
        }
    }
    post {
        always {
            emailext body: '''<!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            <title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>
            </head>

            <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"
                offset="0">
                <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
                    <tr>
                        本邮件由系统自动发出，无需回复！<br/>
                        大家好，以下为 ${PROJECT_NAME } 项目构建信息</br>
                        <td><font color="#CC0000">构建结果 - ${BUILD_STATUS}</font></td>
                    </tr>
                    <tr>
                        <td><br />
                        <b><font color="#0B610B">构建信息</font></b>
                        <hr size="2" width="100%" align="center" /></td>
                    </tr>
                    <tr>
                        <td>
                            <ul>
                                <li>项目名称 ： ${PROJECT_NAME}</li>
                                <li>构建编号 ： 第${BUILD_NUMBER}次构建</li>
                                <li>触发原因： ${CAUSE}</li>
                                <li>构建状态： ${BUILD_STATUS}</li>
                                <li>构建日志： <a href="${BUILD_URL}console">${BUILD_URL}console</a></li>
                                <li>构建URL： <a href="${BUILD_URL}">${BUILD_URL}</a></li>
                                <li>测试报告： <a href="${PROJECT_URL}allure">${PROJECT_URL}allure</a></li>
                            </ul>

            <h4><font color="#0B610B">用例情况</font></h4>
            <hr size="2" width="100%" />
            <li>所有用例：${TEST_COUNTS,var="total"}</li><br/>
            <li>成功用例：${TEST_COUNTS,var="pass"}</li><br/>
            <li>失败用例：${TEST_COUNTS,var="fail"}</li><br/>
            <li>跳过用例：${TEST_COUNTS,var="skip"}</li><br/>

            <h4><font color="#0B610B">最近提交(#${GIT_REVISION})</font></h4>
            <hr size="2" width="100%" />
            <ul>
            ${CHANGES_SINCE_LAST_SUCCESS, reverse=true, format="%c", changesFormat="<li>%d [%a] %m</li>"}
            </ul>
            详细提交: <a href="${PROJECT_URL}changes">${PROJECT_URL}changes</a><br/>

                        </td>
                    </tr>
                </table>
            </body>
            </html>
            ''',mimeType: 'text/html', subject: '【${PROJECT_NAME}】pipeline自动化测试报告', to: 'winnie20150701@outlook.com'
        }
    }
}
