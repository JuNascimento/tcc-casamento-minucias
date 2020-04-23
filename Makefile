setup:
	pip install -r requirements.txt

lint:
	@echo "\n##############################################################"
	@echo "########### DEIXA EU VER SE TÁ TUDO CERTO PRIMEIRO ###########\n"
	@pylint *.py

run: lint
	@echo "########### BELEZA, TA TUDO CERTIN. PODE CONTINUAR! ##########\n"
	@echo "\n##############################################################"
	@echo "################## RODANDO MEU TCC LINDÃO ####################\n"
	@python main.py $(IMAGE_1) $(IMAGE_2)
