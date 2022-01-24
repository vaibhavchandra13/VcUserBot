import asyncio
import os
import git
from pyrogram import Client, filters
from pyrogram.types import Message
from config import bot, HNDLR, SUDO_USERS, HEROKU_API_KEY, OFFICIAL_UPSTREAM_REPO, HEROKU_APP_NAME
# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used \n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
BOT_IS_UP_TO_DATE = "the user / bot is up-to-date."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "chagelog: \n\n{changelog}\n"
    "updating ..."
)
NEW_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "updating ..."
)
REPO_REMOTE_NAME = "tmp_upstream_remote"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "No Heroku App Found..."
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/main"
RESTARTING_APP = "Re-Starting Heroku"
# -- Constants End -- #


@Client.on_message(filters.command(["update"], prefixes=HNDLR) & filters.user(SUDO_USERS))
async def updater(client: Client, m: Message):
    status_message = await m.reply_text("Wait...")
    active_branch_name = repo.active_branch.name
    repo = git.Repo.init()
    if HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            # assuming there will be only one heroku application
            # created per account 🙃
            # possibly, ignore premium Heroku users
            heroku_app = HEROKU_APP_NAME
            heroku_git_url = heroku_app.git_url.replace(
                "https://",
                "https://api:" + HEROKU_API_KEY + "@"
            )
            if "heroku" in repo.remotes:
                remote = repo.remote("heroku")
                remote.set_url(heroku_git_url)
            else:
                remote = repo.create_remote("heroku", heroku_git_url)
            remote.push(refspec=HEROKU_GIT_REF_SPEC, force=True)
        else:
            await m.reply(NO_HEROKU_APP_CFGD)

    await status_m.edit(RESTARTING_APP)
    # https://t.me/c/1387666944/94908
    asyncio.get_event_loop().create_task(restart(client, status_message))


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += "•["
        out_put_str += repo_change.committed_datetime.strftime(d_form)
        out_put_str += "]: "
        out_put_str += f"{repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def restart(client, message):
    await client.restart()
    await message.edit(
        "restarted! "
    )
