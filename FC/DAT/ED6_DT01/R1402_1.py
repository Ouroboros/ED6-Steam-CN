import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1402_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1402_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R1402.x'
    header.mapIndex       = 58
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x693
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FormationDelMember(0x0D, 0xFF)
    ClearChrFlags(0x0008, 0x0080)
    OP_28(0x000F, 0x04, 0x10)
    SetChrPos(0x0101, 2200, 4000, 17880, 270)
    SetChrPos(0x0102, 3120, 4000, 16810, 270)
    SetChrPos(0x0103, 3250, 4000, 17800, 285)
    SetChrPos(0x0008, -200, 4000, 17880, 90)
    CameraMove(20070, 0, 19800, 0)
    OP_6C(315000, 0)
    CameraSetDistance(4000, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_00EE')
    def lambda_00EE():
        OP_69(0x0101, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_00EE)

    @scena.Lambda('lambda_00FC')
    def lambda_00FC():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_00FC)

    @scena.Lambda('lambda_010C')
    def lambda_010C():
        CameraSetDistance(3000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_010C)

    Sleep(7000)

    TerminateThread(0x0009, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0150151129V#130F……呀，你们又帮了我一次啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151130V如果没有你们，\n',
            '我可能早就没命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151131V虽然我的研究经费很少，\n',
            '不过还是要拿出一些给协会作报答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151132V#007F你现在才这么说，\n',
            '一开始就委托游击士不就没事了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0150151133V#130F是啊……\n',
            '下次我一定会好好反省这点的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150151134V那么我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 1000, 4000, 16100, 2000, 0x00)

    @scena.Lambda('lambda_026D')
    def lambda_026D():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_026D')

    DispatchAsync2(0x0101, 0x0001, lambda_026D)

    @scena.Lambda('lambda_027E')
    def lambda_027E():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_027E')

    DispatchAsync2(0x0102, 0x0001, lambda_027E)

    @scena.Lambda('lambda_028F')
    def lambda_028F():
        ChrTurnDirection(0x0103, 0x0008, 0)
        Yield()

        Jump('lambda_028F')

    DispatchAsync2(0x0103, 0x0001, lambda_028F)

    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151135V#023F等一下，\n',
            '不把你送回城里真的没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '#0150151136V#130F哈哈哈，\n',
            '送到这里就可以了，\n',
            '而且我的荷包已经空空如也了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0150151137V#132F那就这样吧……\n',
            '希望我们有缘再会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_037B')
    def lambda_037B():
        CameraMove(2910, 4000, 17460, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_037B)

    ChrWalkTo(0x0008, 1060, 1200, 9530, 2000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0008, 0x02)

    ChrTalk(
        0x0102,
        (
            '#0020151138V#014F……真是个不可思议的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151139V#501F咦，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151140V我觉得他就是那种典型的学者嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151141V一旦集中注意力做某件事情，\n',
            '就会无视周围情况的那种类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151142V#018F…………这说的不是你自己吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151143V#009F哼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151144V我才不是这样呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151145V#026F不过，虽然外表看起来只是个学者，\n',
            '但说不定是个很厉害的人物哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151146V不管怎么说，\n',
            '他敢孤身一人来这种地方也算不简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151147V#007F就算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151148V到头来还不是要靠我们帮忙，\n',
            '不然就陷入绝境了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151149V#020F这也就是我们游击士的职责所在了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151150V那么，\n',
            '我们这就回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【琥珀之塔的可疑人物】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
