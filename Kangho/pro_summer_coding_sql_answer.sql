select game_users.id as 'USER_ID', ifnull(c.total_count, 0) as 'PURCHASE_COUNT', ifnull(c.total_sum, 0) as 'TOTAL_PRICE'
from game_users left outer join (select purchases.user_id as 'id', sum(characters.price) as 'total_sum', count(*) as 'total_count' from
purchases join characters on purchases.item=characters.name
group by purchases.user_id) as c on game_users.id=c.id
group by game_users.id, c.total_count, c.total_sum;