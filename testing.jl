using Debugger

function running(word)
	if word == "this"
		@bp
	end
	print(word)
end

function main()
	running("helloooo")
	running("this")
end

@run main()