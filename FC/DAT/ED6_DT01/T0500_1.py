import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0500_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0500_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0500.x'
    header.mapIndex       = 18
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xCFF
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
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x0101, -4900, 0, -22400, 90)
    SetChrPos(0x0102, -4900, 0, -24400, 90)
    SetChrPos(0x0008, 3000, 0, -22400, 270)
    SetChrPos(0x0009, 3000, 0, -24400, 270)
    ClearChrFlags(0x000A, 0x0008)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -1000, 0, -20400, 180)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_6C(45000, 0)
    CameraSetDistance(2500, 0)
    CameraMove(-20400, 0, -18400, 0)
    FadeIn(3000, 0)
    CreateThread(0x000A, 0x01, 0x01, 0x0001)
    CreateThread(0x000A, 0x02, 0x01, 0x0002)
    OP_6C(315000, 6000)
    Sleep(1500)

    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)

    ChrTalk(
        0x000A,
        (
            '#1130150325V那么，训练现在开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150326V全体，向前五步走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x02, 0x01, 0x0003)
    CreateThread(0x0009, 0x02, 0x01, 0x0004)
    CreateThread(0x0102, 0x02, 0x01, 0x0005)
    CreateThread(0x0101, 0x02, 0x01, 0x0006)
    Sleep(5000)

    ChrTalk(
        0x000A,
        (
            '#1130150327V预备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    SetChrPos(0x0011, -1900, 0, -22400, 90)
    ClearChrFlags(0x0011, 0x0008)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0101, 0x0008)
    SetChrFlags(0x0101, 0x0040)
    SetChrPos(0x0012, -1900, 0, -24400, 90)
    ClearChrFlags(0x0012, 0x0008)
    ClearChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0102, 0x0008)
    SetChrFlags(0x0102, 0x0040)
    SetChrPos(0x000F, 0, 0, -22400, 270)
    ClearChrFlags(0x000F, 0x0008)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    SetChrFlags(0x0008, 0x0040)
    SetChrPos(0x0010, 0, 0, -24400, 270)
    ClearChrFlags(0x0010, 0x0008)
    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    SetChrFlags(0x0009, 0x0040)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#1120150328V我好紧张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1110150329V虽然明知道是训练……\n',
            '可是感觉好害怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 135, 400)

    ChrTalk(
        0x000A,
        (
            '#1130150330V现在是在训练中。\n',
            '不许窃窃私语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150331V要把它当作真正的战斗一样全神贯注！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#1130150332V艾丝蒂尔、约修亚，\n',
            '你们二位不必手下留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010150333V#006F嗯，我一开始就没打算留情☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020150334V#012F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#1110150335V怕怕～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '#1130150336V开战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003ED, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    PlayBGM(16)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_406'),
        (0x00000002, 'loc_7A8'),
        (0x00000001, 'loc_7A8'),
        (-1, 'loc_A7E'),
    )

    def _loc_406(): pass

    label('loc_406')

    FadeIn(2000, 0)
    SetChrPos(0x0013, 0, 0, -22400, 270)
    SetChrPos(0x0014, 0, 0, -24400, 270)
    SetChrSubChip(0x0013, 3)
    SetChrSubChip(0x0014, 3)
    ClearChrFlags(0x0013, 0x0008)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0008)
    ClearChrFlags(0x0014, 0x0080)
    SetChrFlags(0x000F, 0x0008)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0008)
    SetChrFlags(0x0010, 0x0040)
    SetChrPos(0x0101, -1900, 0, -22400, 90)
    SetChrPos(0x0102, -1900, 0, -24400, 90)
    ClearChrFlags(0x0101, 0x0008)
    ClearChrFlags(0x0102, 0x0008)
    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0011, 0x0008)
    SetChrFlags(0x0012, 0x0008)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    OP_0D()
    Sleep(700)

    OP_28(0x0008, 0x01, 0x0002)
    OP_2C(0x0008, 0x00C8)
    OP_2B(0x0008, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#1130150337V好，到此为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150338V训练结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1120150339V疼死我了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1110150340V终于、终于结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150341V#010F辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150342V#007F唉，真是可悲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150343V你们这样还算是士兵吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0013, 0x03, 0x00, 2000)
    SetChrFlags(0x0013, 0x0008)
    SetChrFlags(0x0013, 0x0080)
    SetChrChipByIndex(0x0008, 5)
    ClearChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0008, 0x0040)

    ChrTalk(
        0x0008,
        (
            '#1120150344V真、真是烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120150345V不要把我和\n',
            '你这样的疯丫头相提并论！',
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
            '#0010150346V#005F什么，疯、疯丫头～～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150347V够了，斯科特。\n',
            '训练已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150348V#017F艾丝蒂尔你也要冷静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150349V#009F哼～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#1130150350V……斯科特、哈罗德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150351V刚才艾丝蒂尔的话\n',
            '可是普通市民的心声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150352V你们觉得现在的自己能够保护市民的安全吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150353V自己好好地\n',
            '思考一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120150354V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1110150355V…………好、好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A7E')

    def _loc_7A8(): pass

    label('loc_7A8')

    FadeIn(2000, 0)
    SetChrPos(0x0015, -1900, 0, -22400, 90)
    OP_99(0x0015, 0x03, 0x03, 0)
    ClearChrFlags(0x0015, 0x0008)
    ClearChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0011, 0x0008)
    SetChrPos(0x0102, -1900, 0, -24400, 90)
    ClearChrFlags(0x0102, 0x0008)
    ClearChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0012, 0x0008)
    SetChrFlags(0x0012, 0x0040)
    SetChrChipByIndex(0x0008, 5)
    SetChrChipByIndex(0x0009, 5)
    ClearChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000F, 0x0008)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0008)
    SetChrFlags(0x0010, 0x0040)
    OP_0D()
    Sleep(700)

    OP_28(0x0008, 0x01, 0x0004)

    ChrTalk(
        0x000A,
        (
            '#1130150337V好，到此为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150338V训练结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0010150358V#007F好疼啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0015, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150359V#017F我们输了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150360V太大意了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1110150361V呼～呼～呼……\n',
            '终、终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120150362V我已经一步都走不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#1130150363V斯科特，你怎么能这么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150364V假如这是真正的战斗，\n',
            '现在下一批敌人就已经出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 0)
    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#1120150365V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1110150366V…………是，队长说的是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150350V……斯科特、哈罗德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150368V你们觉得现在的自己\n',
            '能够保护市民的安全吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1130150369V你们需要\n',
            '好好地反省自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 0)
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#1120150370V对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A7E')

    def _loc_A7E(): pass

    label('loc_A7E')

    ChrTalk(
        0x000A,
        (
            '#1130150371V嗯，今天的事就不要放在心上了，\n',
            '以后努力完成任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    FadeOut(3000, 0, -1)
    OP_28(0x0008, 0x01, 0x4000)
    NewScene('ED6_DT01/T0510._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0xADD
@scena.Code('Init')
def Init():
    CameraSetDistance(2800, 6000)

    Return()

# id: 0x0002 offset: 0xAE7
@scena.Code('ReInit')
def ReInit():
    CameraMove(-1600, 0, -22400, 6000)

    Return()

# id: 0x0003 offset: 0xAF9
@scena.Code('func_03_AF9')
def func_03_AF9():
    Sleep(500)

    ChrMoveToRelative(0x0008, -600, 0, 0, 2000, 0x00)
    Sleep(340)

    ChrMoveToRelative(0x0008, -600, 0, 0, 2000, 0x00)
    Sleep(330)

    ChrMoveToRelative(0x0008, -600, 0, 0, 2000, 0x00)
    Sleep(340)

    ChrMoveToRelative(0x0008, -600, 0, 0, 2000, 0x00)
    Sleep(335)

    ChrMoveToRelative(0x0008, -600, 0, 0, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0xB77
@scena.Code('func_04_B77')
def func_04_B77():
    Sleep(700)

    ChrMoveToRelative(0x0009, -600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0009, -600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0009, -600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0009, -600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0009, -600, 0, 0, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0xBF5
@scena.Code('func_05_BF5')
def func_05_BF5():
    Sleep(550)

    ChrMoveToRelative(0x0102, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0102, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0102, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0102, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0102, 600, 0, 0, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0xC73
@scena.Code('func_06_C73')
def func_06_C73():
    Sleep(550)

    ChrMoveToRelative(0x0101, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0101, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0101, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0101, 600, 0, 0, 2000, 0x00)
    Sleep(300)

    ChrMoveToRelative(0x0101, 600, 0, 0, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
