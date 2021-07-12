class LottoController < ApplicationController
    def index
		@byunsu = [*1..45]
		@lotto = @byunsu.sample(6).sort
	end
end
