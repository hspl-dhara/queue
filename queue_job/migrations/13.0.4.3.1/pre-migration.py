# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.drop_columns(
        env.cr, [("queue_job", "parent_id")],
    )

    openupgrade.delete_records_safely_by_xml_id(
        env, ["queue_job.view_queue_job_form"],
    )
