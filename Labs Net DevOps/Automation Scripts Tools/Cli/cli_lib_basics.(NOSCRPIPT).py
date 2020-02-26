    #cli.cli(commands) - executes one or several CLI commands delimited by a space and a semicolon
    # " ;". Returns CLI output. The commands are executed from the privileged EXEC mode.

      output = cli.cli("show version ; show ip int brief")
      print(output[:100]) # prints first 100 symbols of the output

       print(output[-162:]) # prints the last 162 symbols of the output

    #cli.clip(commands) - executes one or several CLI commands similar to cli.cli,
    # however instead of returning the result, it prints it. Usually not used for scripts.

     cli.clip("show memory statistics")

    #cli.execute(command) and cli.executep(command)
    # - similar to cli.cli and cli.clip except execute can run only one command

      cli.executep("show platform software status control-processor brief")

      cli.executep("show platform software status control-processor brief ; show version")

      #You may not run multiple commands using execute().:
      #There was a problem running the command: "show platform software status control-processor brief ; show version"

    cli.configure(commands) and cli.configurep(commands) -

    # applies the configuration commands to the device and returns a list of results (or prints). commands is either a string with one or multiple commands separated by the new-line or an iterable with a set of configuration commands.

        #Let's explore how to use cli.configure, to configure a loopback:

        cli.configurep(["interface Loopback1000", "description DevNet"])

        #Let's verify that it is now configured:

    cli.clip("show run int Loopback1000")
