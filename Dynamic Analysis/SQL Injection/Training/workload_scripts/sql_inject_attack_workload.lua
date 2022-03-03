require "socket"
math.randomseed(socket.gettime()*1000)
math.random(); math.random(); math.random()

request = function()
  local method = "POST"
  -- Use your cluster-ip here:
  local path = "http://10.10.1.201:8082/api/sqlquery"
  local headers = {}
  headers["Content-Type"] = "application/json;charset=UTF-8"
  local x = math.random(1,1000000)
  local body1 = [[ {"user_id":"UPDATE users SET first_name='Adi]]
  local body2 = [[', last_name='Kiran]]
  local body3 = [[' WHERE user_id =]]
  local body4 = [["} ]]
  local body = body1..x..body2..x..body3..x..body4
  return wrk.format(method, path, headers, body)
end