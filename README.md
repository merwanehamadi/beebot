# BeeBot

BeeBot is your personal worker bee, an Autonomous AI Assistant designed to perform a wide range of practical tasks
autonomously.

<p align="center">
<img src="https://eriklp.com/mascot.png" alt="BeeBot Mascot"  align="center" />
</p>

## Status

BeeBot is currently a work in progress and should be treated as an early stage research project. Its focus is not on
production usage at this time. Please be patient as the foundations are still constantly shifting. The world of AI moves
fast, and this project needs to move fast to keep up.

## Installation

To get started with BeeBot, you can clone the repo to your local machine and install its dependencies using `poetry`.
These instructions may vary depending on your local development environment.

```bash
git clone https://github.com/AutoPackAI/beebot.git
cd beebot
./setup.sh
```

Windows is officially unsupported but it may work. PRs are welcome for Windows compatibility but will not be a primary
focus.

### Persistence

If you would like to enable persistence, start a Postgres database (or use your own), with `docker compose up -d`.

Then, set the `DATABASE_URL` environment variable in your .env file. If you're using docker, you can set this
to `DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres`.

## Running

### CLI

To use the CLI run:

```bash
poetry run beebot
```

### API (via [e2b](https://www.e2b.dev/))

To start the server run:

```bash
uvicorn beebot.initiator.api:create_app --factory --timeout-keep-alive=300
```

If you're doing development on BeeBot itself, you may want to use this command:

```bash
uvicorn beebot.initiator.api:create_app --factory --reload  --timeout-graceful-shutdown=3 --timeout-keep-alive=300
```

and then you can call the API using the following commands:

To **create a task** run:

```bash
curl --request POST \
  --url http://localhost:8000/agent/tasks \
  --header 'Content-Type: application/json' \
  --data '{
	"input": "Write '\''hello world'\'' to hi.txt"
}'
```

You will get a response like this:

```json
{
  "input": "Write 'hello world' to hi.txt",
  "task_id": "103",
  "artifacts": []
}
```

Then to **execute one step of the task** copy the `task_id` you got from the previous request and run:

```bash
curl --request POST \
  --url http://localhost:8000/agent/tasks/<task-id>/steps
```

### Websocket Connection

To receive a stream of changes to all the data models in BeeBot, you can subscribe to the websocket connection at
the `/notifications` endpoint with the same host/port as the web api, e.g. ws://localhost:8000/notifications. Use your
favorite websocket testing tool to try it out. (I like [Insomnia](https://insomnia.rest/))

### Web Interface

We are working on a web interface using Node.js (Remix)

## Philosophy

BeeBot's development process is guided by a specific philosophy, emphasizing key principles that shape its development
and future direction.

### Priorities

The development of BeeBot is driven by the following priorities, always in this order:

1. Functionality: BeeBot aims to achieve a high success rate for tasks within its range of _expected_ capabilities.
2. Flexibility: BeeBot strives to be adaptable to a wide range of tasks, expanding that range over time.
3. Reliability: BeeBot focuses on reliably completing known tasks with predictability.
4. Efficiency: BeeBot aims to execute tasks with minimal steps, optimizing both time and resource usage.
5. Convenience: BeeBot aims to provide a user-friendly platform for task automation.

### Principles

To achieve these priorities, BeeBot follows the following principles:

- Tool-focused: BeeBot carefully selects and describes tools, ensuring their reliable use by LLMs. It
  will utilize [AutoPack](https://autopack.ai) as the package manager for its tools.
- LLM specialization: BeeBot will leverage a variety of LLMs best suited for different tasks, while OpenAI remains the
  primary LLM for planning and decision-making.
- Functionality and flexibility first: BeeBot prioritizes functionality and flexibility over developer quality-of-life,
  which may limit support for specific platforms and other deployment conveniences.
- Unorthodox methodologies: BeeBot employs unconventional development approaches to increase development speed, such as
  the absence of unit tests. Instead, end-to-end tests are used, ensuring the entire system works together as expected.
- Proven concepts: BeeBot adopts new concepts only after they have been proven to enhance its five priorities.
  As a result, it does not have complex memory or a tree of thought.

## Documentation

For further information on the architecture and future plans of BeeBot, please refer to the `docs/` directory. The
documentation is currently very light, but will evolve alongside the project as new insights and developments emerge.
Contributions and feedback from the community are highly appreciated.
