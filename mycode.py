
self.object_list = None

    # 임시 장애물 나타내기
    def object_line(self, start, end, height, img):
        for x in range(start, end, 32):
            object = arcade.Sprite(img, char_scaling)
            object.center_x = x
            object.center_y = height
            self.object_list.append(object)

    # 임시 코인 나타내기
    def coin_line(self, start, end, height, img):
        for x in range(start, end, 32):
            coin = arcade.Sprite(img, char_scaling)
            coin.center_x = x
            coin.center_y = height
            self.coin_list.append(coin)

    #player스프라이트 처음위치에서 재시작 , 코인도 재생성
    def player_restart(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite.center_x = 32
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_line(192, 222, 160, "pic/lazer/lazer.png")

        
         # 장애물 임시로 사용
        self.object_line(128, 160, 160, "pic/object_interact/thorn.png")
        #coin sprite 임시로 lazer사용
        self.coin_line(192, 222, 160, "pic/lazer/lazer.png")

        
        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()

        #object랑 player랑 충돌 시
        object_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.object_list)
        #player스프라이트 삭제후 재생성
        for object in object_hit_list:
            self.player_sprite.remove_from_sprite_lists()
            self.player_restart()


             #spring 과 player가 충돌시.
        spring_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.spring_list)
        
             # 스프링에 닿았을 경우
        if self.player_sprite.center_y <= -128:
            self.player_sprite.remove_from_sprite_lists()
            self.player_restart()
            
            #스프링에 닿았을 경우 캐릭터가 점프를 2배높이
    def spring_act(self):
        if self.physics_engine.can_jump():
            self.player_sprite.change_y = player_jump_speed * 2
            self.physics_engine.increment_jump_counter()
