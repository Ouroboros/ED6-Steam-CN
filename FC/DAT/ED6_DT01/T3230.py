import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3230   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3230.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '提妲',
            x                   = 160,
            z                   = 250,
            y                   = 8840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xD2
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_DE'),
        (-1, 'loc_106'),
    )

    def _loc_DE(): pass

    label('loc_DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 6, 0x51E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EE',
    )

    Event(0, func_05_28A)

    def _loc_EE(): pass

    label('loc_EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 3, 0x523)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_103',
    )

    MapSetFlags(0x10000000)
    Event(0, func_06_8E7)

    def _loc_103(): pass

    label('loc_103')

    Jump('loc_106')

    def _loc_106(): pass

    label('loc_106')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12F',
    )

    ChrSetPos(0x0008, 160, 250, 8840, 0)
    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_03_16D)

    def _loc_12F(): pass

    label('loc_12F')

    Return()

# id: 0x0001 offset: 0x130
@scena.Code('func_01_130')
def func_01_130():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_148',
    )

    OP_B1('t3230_y')

    Jump('loc_151')

    def _loc_148(): pass

    label('loc_148')

    OP_B1('t3230_n')

    def _loc_151(): pass

    label('loc_151')

    PlaySE(161, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x157
@scena.Code('func_02_157')
def func_02_157():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_157')

    def _loc_16C(): pass

    label('loc_16C')

    Return()

# id: 0x0003 offset: 0x16D
@scena.Code('func_03_16D')
def func_03_16D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25F',
    )

    ChrWalkTo(0x00FE, -1350, 250, 7890, 3500, 0x00)
    ChrSetDirection(0x00FE, 270, 300)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    ChrWalkTo(0x00FE, -1380, 250, 6670, 3500, 0x00)
    ChrSetDirection(0x00FE, 270, 300)
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1500)

    ChrWalkTo(0x00FE, 2500, 0, 5650, 3500, 0x00)
    ChrSetDirection(0x00FE, 90, 300)
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1500)

    ChrWalkTo(0x00FE, 550, 250, 6470, 3500, 0x00)
    ChrWalkTo(0x00FE, 160, 250, 8840, 3500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_62(0x0008, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1500)

    Jump('func_03_16D')

    def _loc_25F(): pass

    label('loc_25F')

    Return()

# id: 0x0004 offset: 0x260
@scena.Code('func_04_260')
def func_04_260():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0008,
        (
            '#0070080075V#560F嘿咻嘿咻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x28A
@scena.Code('func_05_28A')
def func_05_28A():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(-1060, 250, 8880, 0)
    FormationDelMember(0x06, 0xFF)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -150, 0, 2440, 0)
    ChrSetPos(0x0101, -740, 0, 1150, 0)
    ChrSetPos(0x0102, 500, 0, 690, 0)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    CameraMove(-1090, 0, 2630, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010080056V#501F哎～这个就是导力泵装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080057V#010F完全看不出是很旧的东西，\n',
            '保养得很干净啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080058V#067F#2P嘿嘿……\n',
            '那是因为爷爷每年\n',
            '都来这里对水泵进行维修啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080059V#060F４０年前，\n',
            '导力器还没完全普及……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080060V为了让大家知道导力器的便利性，\n',
            '就制造了这个东西出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080061V#006F原来是这样啊……\n',
            '所以也就非常有纪念意义对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080062V#019F这些事情，\n',
            '等修理好了再慢慢聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070080063V#061F#2P好的～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_04E3')
    def lambda_04E3():
        CameraMove(-320, 250, 8880, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_04E3)

    @scena.Lambda('lambda_04FB')
    def lambda_04FB():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_04FB')

    DispatchAsync2(0x0101, 0x0002, lambda_04FB)

    @scena.Lambda('lambda_050C')
    def lambda_050C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_050C')

    DispatchAsync2(0x0102, 0x0002, lambda_050C)

    @scena.Lambda('lambda_051D')
    def lambda_051D():
        ChrWalkTo(0x00FE, 1200, 250, 7780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_051D)

    Sleep(1000)

    @scena.Lambda('lambda_053D')
    def lambda_053D():
        ChrWalkTo(0x00FE, -170, 0, 4930, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_053D)

    Sleep(500)

    @scena.Lambda('lambda_055D')
    def lambda_055D():
        ChrWalkTo(0x00FE, 1260, 0, 4420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_055D)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080064V#064F唔……\n',
            '首先要检查一下引擎部件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 610, 250, 8820, 3000, 0x00)
    ChrSetDirection(0x0008, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080065V#062F如果没问题的话，\n',
            '就开始检查推进器和配管……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -1320, 250, 7960, 3000, 0x00)
    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080066V#501F啊，提妲。\n',
            '有需要的话我们也可以帮忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080067V#560F啊，没关系呢。\n',
            '我自己一个人就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080068V艾丝蒂尔姐姐，\n',
            '你们先去旅馆休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080069V#064F考虑到气穴现象和\n',
            '水击作用的可能性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -1550, 250, 6380, 3000, 0x00)
    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0070080070V#063F#1P嗯，还有还有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080071V#065F#1P啊，脉冲器也有问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    @scena.Lambda('lambda_07CF')
    def lambda_07CF():
        CameraMove(-490, 0, 6860, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_07CF)

    ChrWalkTo(0x0008, 160, 250, 8840, 4000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010080072V#506F看来就算我们呆在这里，\n',
            '也完全帮不上什么忙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080073V#010F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080074V还是先听提妲的，\n',
            '我们回旅馆等一会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x00A3, 7, 0x51F))
    OP_28(0x0040, 0x01, 0x0010)
    OP_28(0x0028, 0x04, 0x40)
    OP_28(0x0029, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CA',
    )

    OP_28(0x002A, 0x04, 0x40)

    def _loc_8CA(): pass

    label('loc_8CA')

    OP_28(0x002C, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DF',
    )

    OP_28(0x0031, 0x04, 0x40)

    def _loc_8DF(): pass

    label('loc_8DF')

    OP_28(0x0032, 0x04, 0x40)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x8E7
@scena.Code('func_06_8E7')
def func_06_8E7():
    EventBegin(0x00)
    TerminateThread(0x0008, 0xFF)
    MapClearFlags(0x00000001)
    CameraMove(-10, 250, 8880, 0)
    ChrSetFlags(0x0008, 0x0080)
    FormationAddMember(0x06, 0xFF)
    ChrSetPos(0x0107, 160, 250, 8840, 0)
    ChrSetPos(0x0101, -490, 0, 870, 0)
    ChrSetPos(0x0102, 670, 0, 620, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070080230V#063F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_097E')
    def lambda_097E():
        ChrWalkTo(0x00FE, -510, 0, 5070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_097E)

    Sleep(500)

    @scena.Lambda('lambda_099E')
    def lambda_099E():
        ChrWalkTo(0x00FE, 630, 0, 4760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_099E)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0107, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080231V#501F提妲，\n',
            '修理已经完成了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0107, 180, 800)

    ChrTalk(
        0x0107,
        (
            '#0070080232V#064F#2P啊……\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A71')
    def lambda_0A71():
        CameraMove(-80, 250, 7500, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0A71)

    ChrWalkTo(0x0107, 150, 250, 6410, 2000, 0x00)
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070080233V#067F#2P嘿嘿……\n',
            '刚刚才完成了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080234V不过还没有确认\n',
            '热水是不是运送过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080235V#006F没问题了，\n',
            '广场井里的热水都满满的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080236V#010F故障是什么原因造成的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080237V#560F#2P那个啊……\n',
            '其实水泵的装置本身\n',
            '并没有什么太大的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080238V不过回旋螺丝上的曲柄轴\n',
            '锈蚀折断了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080239V我换了个防锈的零件，\n',
            '已经没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080240V#001F是吗，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080241V#019F那我们就回旅馆，\n',
            '把小屋的钥匙还给老板娘吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080242V#061F#2P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00A4, 4, 0x524))
    OP_28(0x0040, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
